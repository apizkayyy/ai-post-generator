import json

from app.models.schemas import PostRequest

def generate_thread_format(count):

    result=[]

    for i in range(1,count+1):

        result.append(
            {
                "number":i,
                "content":f"Thread {i} content"
            }
        )

    return json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    )

def build_prompt(request: PostRequest):

    thread_template = generate_thread_format(
        request.thread_count
    )

    return f"""

Anda adalah content creator affiliate Malaysia.


Tugas:
hasilkan Threads affiliate post.


IMPORTANT:

Response ONLY JSON.

Jangan gunakan:
- markdown
- ```json
- explanation


Output format mesti ikut struktur ini:


{{
"hooks":[
"hook suggestion 1",
"hook suggestion 2",
"hook suggestion 3"
],


"posts": {thread_template},


"cta":
"final call to action"

}}



Product:
{request.product_name}


Description:
{request.description}


Genre:
{request.genre}


Generate exactly {request.thread_count} posts.


Rules:

- Bahasa Melayu Malaysia
- Santai
- Natural storytelling
- Sesuai untuk Threads
- Jangan nampak terlalu menjual
- Setiap thread mesti sambung cerita
- Thread terakhir fokus kepada CTA
- Gunakan emoji jika sesuai

"""