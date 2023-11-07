drop table items;
drop table categories;

-- Categories
create table categories (
    id serial primary key,
    name varchar(50) not null,
    description text
);

INSERT INTO categories (name, description) values
('Eletronics', 'Gadgets to make life easier'),
('Car Parts', 'Expensive stuff for a box with four wheels'),
('Sports', 'Get out and play!'),
('Video Games', 'Stay in and play!')
;

create table items (
    id serial primary key,

    name varchar(200) not null,
    description text not null,
    category_id integer not null,

    foreign key (category_id) references categories (id)
);
