################################################################################
# ML > Supervised Learning > Trees
################################################################################

# load packages



using DecisionTree

using Random, Statistics


X, y = load_data("digits")

X

y

digits = [X y]

vscodedisplay(digits)

#define function to split data

function perclass_splits(y, percent)
    uniq_class = unique(y)
    keep_index = []
    for class in uniq_class
        class_index = findall(y .== class)
        row_index = randsubseq(class_index, percent)
        push!(keep_index, row_index...)
    end
    return keep_index
end

# split data between train and test

Random.seed!(123)

train_index = perclass_splits(y, 0.75)

test_index = setdiff(1:length(y), train_index)

# split features

X_train = X[train_index, :]

X_test = X[test_index, :]

# split classes

y_train = y[train_index]

y_test = y[test_index]

################################################################################
# Decision Tree
################################################################################

# run model

model = DecisionTreeClassifier(max_depth = 5)

fit!(model, X_train, y_train)

# print tree

print_tree(model)

# view training data

train = [X_train y_train]

vscodedisplay(train)

# make predictions

y_hat = predict(model, X_test)

# check accuracy

accuracy = mean(y_hat .== y_test)


using MLJ

multiclass_f1score(y_hat, y_test)

MLJ.confusion_matrix(y_test, y_hat)

check = [y_hat[i] == y_test[i] for i in 1:length(y_hat)]

check_display = [y_hat y_test check]

vscodedisplay(check_display)

################################################################################
# Random Forest (bagging)
################################################################################

# run model

model = RandomForestClassifier(n_trees = 5)

fit!(model, X_train, y_train)

# make predictions

y_hat = predict(model, X_test)

# check accuracy

accuracy = mean(y_hat .== y_test)

multiclass_f1score(y_hat, y_test)

# display confusion matrix

MLJ.confusion_matrix(y_test, y_hat)

# display results

check = [y_hat[i] == y_test[i] for i in 1:length(y_hat)]

check_display = [y_hat y_test check]

vscodedisplay(check_display)

# display probability of each prediction

prob = predict_proba(model, X_test)

