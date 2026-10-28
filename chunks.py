def chunk(text, size, overlap=150):
    """
    Questa funzione prende un testo e lo suddivide in blocchi chiamati chunks,

    Questa è una funzione di prova, che prende solamente un testo e lo suddivide in blocchi di size dimensione.
    Verrà implementata una funzione che farà dei chunking intelligenti, che terranno conto della semantica, dei paragrafi o dei titoli
    così da avere dei chunlks più coerenti e leggibili.
    """
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
    if overlap < 0:
        raise ValueError("Overlap must be a non-negative integer.")
    
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += size - overlap  # Move the start index forward by size minus overlap

    return chunks