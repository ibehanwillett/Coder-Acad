drop table items;
drop table categories;
-- Categories
create table categories (
    id serial primary key,
    name varchar(50) not null unique,
    description text
);

insert into categories (name, description) values
    ('Electronics', 'Gadgets to make life easier'),
    ('Car Parts','Expensive stuff for a box with four wheels'),
    ('Sports', 'Get out and play!'),
    ('Video Games', 'Stay in and play!');

-- Items

create table items (
    id serial primary key,
    name varchar(200) not null,
    description text not null,
    category_id integer not null,
    foreign key (category_id) references categories (id) on delete cascade
);

insert into items (name, description, category_id) values
('Skyrim', 'Awesome open-world RPG', 4),
('World of Warcraft', 'Popular MMORPG', 4),
('iPhone', 'Apple''s flagship phone', 1),
('Greg Norman golf clubs', 'At least you can look like a pro', 3)