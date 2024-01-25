select * from Products;
select name, price from Products;
select sum(stock_count) from Products;
select category,sum(stock_count) from Products group by category;
select o.product_id,o.quantity,p.name from Orders_Items o join Products p on p.id=o.product_id;
select sum(o.quantity) as total_quantity,p.name,sum(o.total_price) as total_price from Orders_Items o join Products p on p.id=o.product_id group by p.id;
