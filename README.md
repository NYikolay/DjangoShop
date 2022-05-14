# DjangoShop
____

## Кастомная модель пользователя
### Поля:
1) Email;
2) Password;
3) Username;
4) Wallet;

Отдельным приложением реализована регистрация, авторизация, выход.

## Основные модели

### Продукт ( Product)
#### Поля:
1) Title;
2) Description;
3) Price;
4) Quantity_in_stock;
5) Created_at;
6) Image ( null = True, blank = True);

### Покупка (Purchase)
#### Поля:
1) User (ForeignKey);
2) Product (ForeignKey);
3) Quantity_of_products;
4) Created_at;

### Возврат покупки (ReturnPurchase)
#### Поля:
1) Purchase;
2) Time_of_request;

## Функционал
