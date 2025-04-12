Что нужно сделать:

* [X]  Route выдачи товаров
* [X]  выдачу еды сделайте на вот этот рут **/getProductCards**

> Формат ответа такой {{"product": "Самса", "price":  120}, {"product": "Шава", "price":  250}}

* [ ]  Механизм обработки карзины заказов **/newOrder**

> {
> "Name" : String,
> "Surname" : String,
> "Adress" : String
> "Phone" : String,
> "Cost" : Number,
> "Status" : String,
> "Products" : Array<Int>
> }

* [X]  вход / регистрация запрос

> {
> login: String,
> password: String
> }
>
> Ответ :
>
> {token: String}

* [X]  Добавление в корзину (post)

> /addToCart - рут
> Запрос
> {
> login: String,
> count:Number,
> price:Number,
> product:String
> }

* [X]  Получение корзины (get)

> /getCart - рут
> Запрос
> {
> login: String,
> }
> Ответ:
> {[
> {
> login: String,
> count:Number,
> price:Number,
> imagePath: String,
> product:String
> },
> ...
> ]}
