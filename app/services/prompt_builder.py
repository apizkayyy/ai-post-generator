def build_prompt(request):

    return f"""
Generate a {request.platform} affiliate post.

Product:
{request.product_name}

Description:
{request.description}

Genre:
{request.genre}

Tone:
{request.tone}

Rules:
- Generate exactly {request.thread_count} posts
- Number posts from 1 to {request.thread_count}
- Return only the required JSON structure
"""