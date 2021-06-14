from store.models import Product
from decimal import Decimal

class Basket():
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        """
        Função inicial da classe
        """
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket



    def add(self, product, qty):
        """
        Adicionado produtos na sessão 
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] += int(qty)
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': int(qty)}

        self.save()


    def __iter__(self):
        """
        Função de iteração da classe
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product']= product

        for item in basket.values():
            item['price']= Decimal(item['price'])
            item['total_price']=item['price'] * item['qty']
            yield item


    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def get_individual_total_itens(self):
        """
        Retorna a quatidade individual de intes no carrinho, ou seja, quantos itens desconsiderando sua quantidade
        """
        return len(self.basket)

    def get_total_price(self):
        """
        Retorna o valor total dos produtos no carrinho
        """
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())


    def delete(self, product):
        """
           Apaga produtos da sessão
        """
        product_id= str(product)

        if product_id in self.basket:
            del self.basket[product_id]
        self.save()

    def update(self, product, qty):
        """
        Atualiza os valores da sessão
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()

    def save(self):
        """
        Salva os valores da sessão
        """
        self.session.modified = True