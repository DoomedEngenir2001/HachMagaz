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

* [ ]  вход / регистрация запрос

> {
> login: String,
> password: String
> }
>
> Ответ :
>
> {token: String}

* [ ]  Рут /login
* [ ]  Рут /registration
* [ ]  Получение заказов /getOrders

> {
> login: String
> }
>
> Ответ:
>
> {[
> {
> "Name" : String,
> "Surname" : String,
> "Adress" : String,
> "Phone" : String,
> "Cost" : Number,
> "Status" : String,
> "Products" : Array<Int>
> },
> ...
> ]}

* [ ]  /getAddresses

> {
> login: String
> }
>
> Ответ:
> {[
> address: String,
> ...
> ]}

* [ ]  Добавление в корзину (post) /addToCart

> {
> login: String,
> count:Number,
> price:Number,
> product:String
> }

* [ ]  Получение корзины (get) /getCart

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
