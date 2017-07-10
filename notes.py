def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    #use the distance function to compute the distance between each centroid
    #and the given location. Make an array of arrays that has the corresponding 
    #centroid and its location. Somehow iterate through this array of arrays checking 
    #for the minimumum distance, can probably also just use the min function, but i couldnt figure it out
    #and went for this easy way out

def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """
    #sorry i cant explain something i dont know


def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    # you want to find the centroid of the cluster given to you 
    # which means you want to find the mean of something. Figure out how to 
    #iterate through cluster and how to get the locations of each restaurant in cluster
