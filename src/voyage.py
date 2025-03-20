import voyageai
import numpy as np

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")


###
def test_basic():
    texts = ["Hello World", "I am Vishal"]

    result = vo.embed(texts, model="voyage-3", input_type="document")
    print(result.embeddings[0])
    print(result.embeddings[1])


def test_advanced():
    documents = [
        "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
        "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
        "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
        "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
        "Apple’s conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
        "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature."
    ]

    # Embed the documents
    doc_embds = vo.embed(
        documents, model="voyage-3", input_type="document"
    ).embeddings
    query = "When is Apple's conference call scheduled?"

    # Embed the query
    query_embd = vo.embed(
        [query], model="voyage-3", input_type="query"
    ).embeddings[0]

    # Compute the similarity
    # Voyage embeddings are normalized to length 1, therefore dot-product
    # and cosine similarity are the same.
    similarities = np.dot(doc_embds, query_embd)

    retrieved_id = np.argmax(similarities)
    print(documents[retrieved_id])


test_advanced()




