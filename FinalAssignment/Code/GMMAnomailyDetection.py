import GlobalParameters
from sklearn.mixture import GaussianMixture
from Dataset2 import Dataset2
import numpy as np
from GMM import GMMAlgorithm
"https://towardsdatascience.com/understanding-anomaly-detection-in-python-using-gaussian-mixture-model-e26e5d06094b"

def get_anomalous_indices(dataset, anomalous_threshold, random_state=GlobalParameters.randomState):
    
    train_df = dataset.get_data_frame()

    ############################# create sklearn object.
    gmm_obj = GaussianMixture(n_components = dataset.get_n_classes(), covariance_type = 'full', random_state=random_state)
    
    ############################# fit model.
    gmm_obj.fit(train_df)

    probabilities = gmm_obj.predict_proba(train_df)

    
    
    ############################# calculate the product of (1 - probability of being in cluster k) - the probability of not being in cluster k. See reference picture.
    ############################# we're left with a list of probabilities of being generated by any Gaussian distribution. Points with probability
    ############################# above a threshold can be considered anomalous.
    # probability_complement_product_array = 1 - np.prod(1 - probabilities, axis = 1)
    # 
    # print(probability_complement_product_array)
    # 
    # anomalous_indices = probability_complement_product_array < anomalous_threshold
    # print(probability_complement_product_array[probability_complement_product_array < anomalous_threshold])
    # 
    # 
    # to get the indices we can remove and paint the points that aren't there after all of the iterations.
    # can crete a seprate df using concat and find the row indices with iloc.


dataset = Dataset2()
dataset.prepareDataset()

gmm = GMMAlgorithm(dataset.get_n_classes())
gmm.get_anomalous_indices_silhouette_coefficients(dataset)

# get_anomalous_indices(dataset, 0.8)

