# Рекомендаційна система книг – базовий аналіз даних

# 1. Імпорт бібліотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Завантаження CSV
books = pd.read_csv('data/books.csv')       # Дані про книги
ratings = pd.read_csv('data/ratings.csv')   # Рейтинги користувачів
users = pd.read_csv('data/users.csv')       # Дані про користувачів

# 3. Попередній перегляд даних
print("=== Книги ===")
print(books.head())
print("\n=== Рейтинги ===")
print(ratings.head())
print("\n=== Користувачі ===")
print(users.head())

# 4. Перевірка на пропуски
print("\n=== Пропуски у даних ===")
print("Books:\n", books.isnull().sum())
print("Ratings:\n", ratings.isnull().sum())
print("Users:\n", users.isnull().sum())

# 5. Основні статистики
print("\n=== Статистика даних ===")
print("Books:\n", books.describe(include='all'))
print("Ratings:\n", ratings.describe())
print("Users:\n", users.describe())

# 6. Візуалізація популярності книг
# Кількість оцінок для кожної книги
top_books = ratings.groupby('ISBN')['Book-Rating'].count().sort_values(ascending=False).head(10)
top_books = top_books.reset_index()

# Об'єднання з назвами книг
top_books = top_books.merge(books[['ISBN', 'Book-Title']], on='ISBN')

# Побудова графіка
plt.figure(figsize=(12,6))
sns.barplot(data=top_books, x='Book-Title', y='Book-Rating', palette='viridis')
plt.xticks(rotation=45, ha='right')
plt.title('Топ-10 найпопулярніших книг за кількістю оцінок')
plt.xlabel('Назва книги')
plt.ylabel('Кількість оцінок')
plt.tight_layout()
plt.show()

# 7. Побудова матриці користувач - книга для колаборативної фільтрації
user_book_matrix = ratings.pivot(index='User-ID', columns='ISBN', values='Book-Rating').fillna(0)
print("\nРозмір матриці користувач-книга:", user_book_matrix.shape)
print(user_book_matrix.head())
