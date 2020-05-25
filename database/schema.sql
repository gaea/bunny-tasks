create table "user" (
	id serial primary key,
	name varchar(250)
);

create table task (
	id serial primary key,
	description varchar(250) not null,
	state varchar(250) not null,
	user_id integer not null,
	constraint tasks_user_user_id_fkey foreign key (user_id)
      references "user" (id) match SIMPLE
      on update cascade on delete cascade
);