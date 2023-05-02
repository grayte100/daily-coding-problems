# load data

################################################################################
# ML > SL > Classification > Naive Bayes
################################################################################
#Was trying to use the dataset for SVM for Naive Bayes Classifier to see
#how well it performs

using RDatasets
using LinearAlgebra, Random, Statistics

# load data

iris = dataset("datasets", "iris")

vscodedisplay(iris)

X = Matrix(iris[:, 1:4])



# define function to split data (source: Huda Nassar)

#function perclass_splits(y, percent)
    #uniq_class = unique(y)
    #keep_index = []
    #for class in uniq_class
       # class_index = findall(y .== class)
       # row_index = randsubseq(class_index, percent)
       # push!(keep_index,row_index...)
    #end
    #return keep_index
#end

#split data between train and test 

#Random.seed!()

#train_index = perclass_splits(y, 0.67)

#test_index = setdiff(1:length(y), train_index)

# split matrix into vectors

x1 = X[:, 1]
x2 = X[:, 2]
x3 = X[:, 3]
x4 = X[:, 4]

y = iris.Species

uniq_x1 = unique(x1)
uniq_x2 = unique(x2)
uniq_x3 = unique(x3)
uniq_x4 = unique(x4)

uniq_y = unique(y)

# calculate probabilities for "setosa", "versicolor and "virginica" outputs

len_y = length(y)

len_setosa = count(x -> x == "setosa", y)

len_versicolor = count(x -> x == "versicolor", y)

len_virginica = count(x -> x == "virginica", y)


p_setosa = len_setosa / len_y

p_versicolor = len_versicolor / len_y

p_virginica = len_virginica/len_y

# split "setosa", "versicolor" and "virginica" into separate matrices

data_setosa = iris[iris[:, 5] .== "setosa", :]

data_versicolor = iris[iris[:, 5] .== "versicolor", :]

data_virginica = iris[iris[:, 5] .== "virginica", :]

# count features in data_setosa

len_sunny_yes = count(x -> x == uniq_x1[1], data_yes)
len_overcast_yes = count(x -> x == uniq_x1[2], data_yes)
len_rainy_yes = count(x -> x == uniq_x1[3], data_yes)

len_hot_yes = count(x -> x == uniq_x2[1], data_yes)
len_mild_yes = count(x -> x == uniq_x2[2], data_yes)
len_cool_yes = count(x -> x == uniq_x2[3], data_yes)

len_high_yes = count(x -> x == uniq_x3[1], data_yes)
len_normal_yes = count(x -> x == uniq_x3[2], data_yes)

len_false_yes = count(x -> x == uniq_x4[1], data_yes)
len_true_yes = count(x -> x == uniq_x4[2], data_yes)
