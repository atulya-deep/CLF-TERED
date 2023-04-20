# CLF-TERED
Find the Table : A Contrastive Learning-based Approach with Faster RCNN for Establishing Tabular Entity Relationships
# Abstract 
Financial industries rely on a variety of data to understand an organization’s financial health and performance, and analysis of financial statements is used for decision-making and understanding business activities. Financial statements often have complex, unstructured formats, making it difficult to extract useful information for decision-making. Organizing and refining these data is crucial for effective analysis. Previous research in the field of table detection has primarily centred around
object detection methods, with limited exploration of methods for cell-wise information extraction by identifying row and column entities. In order to address this research gap, this paper proposes a novel dataset called TERED (Tabular Entity Relationship Establishment Dataset) to train a model to identify relationships among elements in large financial tables, such as statements and balance sheets, using computer vision techniques which have yet to be fully explored in financial analysis. The dataset contains more than 10,000 tabular data in scanned image and pdf formats and is divided into 12 classes. We trained CLF-RCNN, aContrastive Learning based Faster RCNN model which in turn is a state-of-the-art object detection model on this dataset and achieved an F1 score of 93% for table detection and 74% for identifying tabular entities and relationships. Additionally, we introduced a new loss term influenced by contrastive learning that improves prediction performances with our developed algorithm to return the sequential order of the unordered predictions. Index Terms—Table Detection, Financial dataset, Tabular Entities Relationship Establishment, Row Column Extraction, Contrastive Learning, Faster RCNN.
# Dataset
The dataset contains more than 10k images in different

languages and is annotated within 12 classes, which are:

• parent row: A row having one or more child rows.
They are further divided into bold parent row and
non bold parent row based on the text boldness.

• bold row: A single row with bold text.

• non bold row: A single row with non-bold text.

• sub row: A subpart of a parent row and might in turn
contain further sub rows.

• direct children: A parent row will contain one or more
child rows.

• prime parent: A heading that is connected to all lower level rows and acts as the ancestor to those rows. A prime
parent contains multiple parent rows.

• parent column: A column with one or more child
columns is considered a parent column.

• column: A single column that does not contain any
further child.

• closure row: These signify the net changes (increment or
decrement) in asset, equity, balance, etc. They generally
conclude the financial statements and are an important
part of any financial tables.

• table: The financial table needs to be identified before its
components.

• others: To construct a more generalized dataset, the
others class is included in this dataset, and it does not
contain any tabular entities.
