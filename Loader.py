## Code for loading training sets and creating documents.
import string

from Cluster import *
from make_dataset import create_tokens, create_documents


## homogeneity: for each cluster, what fraction of the cluster is comprised of the largest class?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_homogeneity(result, ['pos','neg'])

def compute_homogeneity(list_of_clusters, list_of_classes) :
    # hlist will be the homogeneity for each cluster.
    hlist = []

    return hlist

## completeness: for the dominant class in each cluster, what fraction
# of that class' members are in that cluster?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_completeness(result, ['pos','neg'])

def compute_completeness(list_of_clusters, list_of_classes) :
    # clist will be the homogeneity for each cluster.
    clist = []

    return clist

if __name__=="__main__" :

    pos_reviews, neg_reviews = create_tokens(10,10, 10)






