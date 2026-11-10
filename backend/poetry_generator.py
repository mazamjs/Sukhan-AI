
from backend.chains import chain


def generate_poetry(
    poetry_type: str,
    theme: str,
    instructions: str = ""
) -> str:

    try:
        response = chain.invoke({
            "poetry_type": poetry_type,
            "theme": theme,
            "instructions": instructions or "Write naturally."
        })

        return response.content

    except Exception as e:
        raise RuntimeError(
            f"Poetry generation failed: {str(e)}"
        ) from e
