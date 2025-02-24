## generate a simple dataset for clustering.
import random
from Document import Document

pos_lexicon = ['cat','dog','fish','monkey','goat','hippo','orangutan','whale','lobster','horse']
neg_lexicon = ['cat','fish','joke','map','right','fly','sled','tiger','hide','float']

# npos - number of positive documents
# nneg - number of negative documents
# length - the length of each document.
def create_tokens(npos, nneg, length) :
    pos_docs = []
    neg_docs = []
    for i in range(npos) :
        d = [random.choice(pos_lexicon) for j in range(length)]
        pos_docs.append(d)
    for j in range(nneg) :
        d = [random.choice(neg_lexicon) for j in range(length)]
        neg_docs.append(d)

    return (pos_docs, neg_docs)


# npos - number of positive documents
# nneg - number of negative documents
# length - the length of each document.

def create_documents(npos, nneg, length) :
    plist, nlist = create_tokens(npos, nneg, length)
    dlist = []
    for item in plist :
        d = Document(true_class='pos')
        d.add_tokens(item)
        dlist.append(d)
    for item in nlist :
        d = Document(true_class='neg')
        d.add_tokens(item)
        dlist.append(d)
    return dlist