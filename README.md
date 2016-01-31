# Deep Thought

Deep Thought is a graphical platform for the visual definition and editing of Deep Neural Networks. The system is a web-based interface that interoperates with leading open source Deep Learning frameworks. Deep Thought provides a cloud‐based graphical interactive solution to design huge complex neural networks, and allow users to experiment with various toolkit in parallel. Users could simply draw the network structure, select algorithms, and upload dataset, then Deep Thought could automatically parse the design, feed into multiple machine learning frameworks, train the model in  backstage and offer evaluations to the front‐end.

#### Team Mentors:

Bhkisha Raj, Rita Singh

#### Team Members:

Wei Jiang (Team Lead), Jingwei Li, Rui Wang, Xi Liu Xinyun Zhao, Xiangzhu Long, Yichen Cai

### Motivation		
					
For data scientists and researchers, they need to design neural networks by feeding text input to toolkits very frequently. However nowadays with the growing popularity of deep learning and convolutional neural networks, text inputs, especially these tailored for various frameworks could cost unnecessary labors even introduce typo bugs. 

Therefore, an interactive tool for designing networks with cross-toolkit backend are desired.		

### Benefits								

For data scientists, they could skip tedious environment setup and text input creation, and focus on the architecture and algorithms of the model. 

For organizations, deep thoughts improves the overall efficiency and productivity, and the cloud-based solution also substitutes cost in fixed asset with operational costs, which is more flexible and manageable. 

### Mechanism

Deep Thought provides a cloud-based graphical interactive solution to design huge complex neural networks, and allow users to experiment with various toolkit in parallel. 

Users could simply draw the network structure, select algorithms, and upload dataset, then Deep Though could automatically parse the design, feed into multiple machine learning frameworks, train the model in backstage and offer evaluations to the front-end. 

### Highlighted Features

* Flexible, self-customized visual interactive environment. 
* High-performance Convolutional Neural Networks serialization and deserialization library which is used for passing description and configuration of Neural Networks through networks.

  We are supporting the following deep learning toolkits: 
   - Tensorflow
   - TBC

* High-performance backend solution that provides training, adjustment, feedback of user-customized models.

### Use Cases

1. Setup
	
System setup should be done before users start use. Users don’t need to setup and launch system.

2. Design a simple neural network
   * User opens browser and input the service URL
   * User creates a whiteboard and gets the simple toolbox.
   * User designs the network on the whiteboard
   * User sets parameters and submits the design
   * The system parses the design and feeds into Caffe
   * Caffe train the neural networks and generate feedbacks
   * The system visualize the feedbacks to user
   * User verify the parameters and functions inside neurons
   * User modify the design and repeat d - g

3. Design a complex neural network
   * User opens browser and input the service URL
   * User creates a whiteboard and gets the powerful toolbox.
   * User designs the network (either draw neurons or layers) on the whiteboard
   * User sets parameters and layer properties, then submits the design
   * The system parses the design and clusters the neurons by layers
   * The system feeds the design into Caffe
   * Caffe train the neural networks and generate feedbacks
   * The system visualize the feedbacks to user
   * User verify the parameters and functions inside neurons and layers
   * User modify the design and repeat d - i

4. Upload and process datasets
   * User opens the board of uploading.
   * User chooses the source of datasets, either upload locally or upload by links.
   * User confirms the datasets.
   * User submits the datasets.
   * Optionally, user selects several features or instances to create a subset
   * The system generate new datasets following users instructions

5. Experiment multiple algorithms
	 
   The interaction is very similar to UC3. 
   * User finalizes the neural networks.
   * User specifies the the algorithms of interest.
   * User submits request.

6. Evaluation and Error Analysis
   * Caffe train the neural networks and generate feedbacks
   * The system visualize the feedbacks to user
   * User views the performance
   * User compares the performances of multiple algorithms and toolkits
   * User reconfigures the parameters or adjust the networks.
   * User resubmits experiment requests.


### Achives

[Demo Day Presentation](https://docs.google.com/presentation/d/1V_JC7z_xxNAV-JFmKlpWs6FCLVP2aCoeuYOM1R0s2Ys/edit#slide=id.geb073114e_0_0) (Dec, 7th, 2015)

[GUI Design](https://github.com/DeepThoughtTeam/D3-Graphic/blob/master/GUI%20Design.md)

[Pipeline](pipeline.png)


