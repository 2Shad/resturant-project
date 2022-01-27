class Table:
    def __init__(self, people):
        self.people = people
        self.bill = []
    

    def order(self, item, price, quantity=1):
        changed = False   
        for billy in self.bill:
            if billy.get('item') == item and billy.get('price') == price:
                # self.bill[self.bill.index({'item': item, 'price': price, 'quantity': quantity})]['quantity'] += quantity
                billy['quantity'] += quantity
                changed = True
                break
        if changed == False:
            self.bill.append({'item': item, 'price': price, 'quantity': quantity})
                


    def remove(self, item, price, quantity):   
        found = False
        for billy in self.bill:
            if billy.get('item') == item and billy.get('price') == price:
                billy['quantity'] -= quantity
                if billy['quantity'] == 0:
                    self.bill.pop(billy)
                found = True
                break
        return found


    def get_subtotal(self):
        subtotal = 0
        for billy in self.bill:
            subtotal += billy['price'] * billy['quantity']
        return subtotal

    def get_total(self, percentage=0.10):
        subtotal = self.get_subtotal()
        service_charge = subtotal * percentage
        total = subtotal + service_charge
        return {'Sub Total': f'£{subtotal:.2f}', 'Service Charge': f'£{service_charge:.2f}', 'Total': f'£{total:.2f}'}

    
    def split_bill(self):
        return self.get_subtotal() / self.people


# table05 = Table(5)
# table05.order('Food1', 10.00, 3)
# table05.order('Food2', 20.00, 1)
# table05.order('Food3', 0.60, 1)
# print(table05.get_total(0.15))