# VECTOR SEARCH

TODO:

* What version of atlas?
* Filters?  

NOTES:

* Choosing the Right Similarity Method
  * If your vectors are normalized: start with Dot Product. Dot product is a computationally cheaper operation compared to cosine similarity and is efficient when vectors are of unit length.
  * If your vectors are not normalized: Evaluate Cosine Similarity or Euclidean Distance in the next step.
* Quantization is available only for 32-bit float vectors.
  * None (Default) – No quantization is applied, preserving full precision. Ideal if accuracy is critical, though it requires more storage.
  * Scalar Quantization – Converts 32-bit floats to int7. This reduces memory requirements substantially with minimal accuracy loss, offering a balance of cost efficiency and precision.
  * Binary Quantization – Converts floats into binary (0 or 1) for maximum memory savings and can improve query latency. Best for use cases where minor precision loss is acceptable, such as high-level categorization.
* Enhancing Query Performance with Filters
  * There seems to be only one filter per index.  

## Resources

* Load Data into Atlas [here](https://www.mongodb.com/docs/atlas/sample-data/#std-label-load-sample-data)
* https://www.mongodb.com/docs/atlas/sample-data/sample-mflix/
* https://www.mongodb.com/blog/post/vector-quantization-scale-search-generative-ai-applications
* https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-overview/
* How to Index Fields for Vector Search [here](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-type/)