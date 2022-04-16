import pandas as pd
data = pd.read_csv('train.csv', index_col="PassengerId")
type (data)

# TODO #1
def get_sex_distrib(data) -> str:
    """
    1. Какое количество мужчин и женщин ехало на параходе? 
    
    Приведите два числа через пробел.
    """
    # data['Sex'].value_counts()
    n_male, n_female = data['Sex'].value_counts()
    return f"{n_male}, {n_female}"

print(get_sex_distrib(data))

# TODO #2
# C = Cherbourg, Q = Queenstown, S = Southampton

def get_port_distrib(data) -> str:
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? 
    Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = data['Embarked'].value_counts()
    return f"{port_S}, {port_C}, {port_Q}"


print(get_port_distrib(data))


####################
x = pd.Series(range(10, 90))

l = [1, 2, 4, 5, 8, 12, 18, 25, 96, 48]
l1 = list(reversed(l))
print(l1)
y = pd.Series(l1)


print(x.corr(y))
####################


# TODO 3
# Посчитайте долю (процент) погибших на параходе (число и процент)?
def calc_death_count(data) -> str:
    count_death, count_lives = data['Survived'].value_counts()
    return f"{count_death}, {count_death / (count_death + count_lives) * 100}"


# TODO 4
# Какие доли составляли пассажиры первого, второго, третьего класса?
def get_class_info(data) -> str:
    first_class = data['Pclass'].loc[data['Pclass'] == 1].count()
    second_class = data['Pclass'].loc[data['Pclass'] == 2].count()
    third_class = data['Pclass'].loc[data['Pclass'] == 3].count()

    all_count = first_class + second_class + third_class

    return f"{first_class/all_count}, {second_class/all_count}, {third_class/all_count}"


# TODO 5
# Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
def corr_sibsp_parch(data) -> float:
    return data['SibSp'].corr(data['Parch'], method='pearson')


# TODO 6
# Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

# возрастом и параметром Survived;
def corr_age_surv(data) -> float:
    return data['Survived'].corr(data['Age'], method='pearson')

# полом человека и параметром Survived;
def corr_sex_surv(data) -> float:
    return data['Survived'].corr(pd.Series([1 if i == 'male' else 0 for i in data['Sex']]), method='pearson')

# классом, в котором пассажир ехал, и параметром Survived.
def corr_class_survived(data) -> float:
    return data['Survived'].corr(data['Pclass'], method='pearson')


# TODO 7
# Посчитайте средний возраст пассажиров и медиану, минимальный и максимальный возраст.
def pass_mean_median(data) -> str:

    mean_age = data['Age'].mean(skipna=True)
    median_age = data['Age'].median(skipna=True)
    return f"{ mean_age }, { median_age }"

# TODO 8
# Посчитайте среднюю цену за билет и медиану
def ticket_mean_median(data) -> str:

    mean_fare = data['Fare'].mean(skipna=True)
    median_fare = data['Fare'].median(skipna=True)

    return f"{ mean_fare} , { median_fare }"

# TODO 9
# Какое самое популярное мужское имя на корабле?
def popular_name(data) -> str:
    
    names = [i.split(', ')[1] for i in data['Name']]
    sorted_names = pd.Series(names).value_counts()
    
    return sorted_names.index[0], sorted_names.iat[0]

# TODO 10 
# Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
def popular_adult_names(data) -> str:

    older_male = data[(data['Age'] > 15) & (data['Sex'] == 'male')]
    older_female = data[(data['Age'] > 15) & (data['Sex'] == 'female')]

    male_names = [i.split(', ')[1] for i in older_male['Name']]
    male_sorted_names = pd.Series(male_names).value_counts()

    female_names = [i.split(', ')[1] for i in older_female['Name']]
    female_sorted_names = pd.Series(female_names).value_counts()
    
    return male_sorted_names.index[0], male_sorted_names.iat[0], female_sorted_names.index[0], female_sorted_names.iat[0]