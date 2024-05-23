# task 2
### Create example db
**CREATE** **TABLE** ext (
    name text,
    status int
);

**CREATE** **TABLE** no_ext(
    name text,
    status int
);

**INSERT** **INTO** no_ext (name, status) 
**VALUES** ('nazv1', 1);
**INSERT** **INTO** no_ext (name, status) 
**INSERT** ('nazv2', 0);
**INSERT** **INTO** **no_ext** (name, status) 
**VALUES** ('nazv5445', 1);


**INSERT** **INTO** ext (name) 
**VALUES** ('nazv1.mp3');
**INSERT** **INTO** ext (name) 
**VALUES** ('nazv2.mp3');
**INSERT** **INTO** ext (name) 
**VALUES** ('nazv5445.mp3');


### Look db content
**SELECT** ***** **FROM** ext;
**SELECT** ***** **FROM** no_ext;

### match same names with no extension 
**SELECT** e.name, e.status, n.status **FROM** ext e **INNER** **JOIN** no_ext n **ON** substring(e.name, n.name)=n.name;

## METHOD 1
#### for better performance set INDEX on column name on both tables.

### using subq
**UPDATE** ext
**SET** status = 
  (
    **SELECT** status 
    **FROM** no_ext n
    **WHERE** substring(ext.name, n.name)=n.name
  );
  
**select** * **from** ext;

drop table ext;
drop table no_ext;
