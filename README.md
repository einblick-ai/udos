# Einblick's UDO repository.

If you would like to add a new UDO in this repo to make it accessible via git syncronization, you can export it from Einblick's UDO editor and add it to this repo. 

The code requirements to add an UDO to this repository are stricter than the ones in the UDO editor. In particular your UDO will need a completly filled `manifest file` and a description in the `operator specification`. Also, you will have to add a unittest folder to your UDO's folder (you can check out this [link](https://gitlab.com/einblick/udos/-/tree/master/operators/dataframe%20manipulation/bottom/test) as a referece).

Please refer to [TableResultWrapper](https://gitlab.com/einblick/montana-api/-/blob/master/src/table/TableResultWrapper.ts) class to learn more about the calls you can make on the tables.
