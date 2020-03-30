# data_json_conllx


将 json 格式数据 转换成 .conllx 格式的数据

json 数据格式:
```
{
    "domain":"weather",
    "entities":[
        {
            "end":2,
            "entity":"地点",
            "length":2,
            "start":0,
            "value":"上海"
        },
        {
            "end":5,
            "entity":"日期",
            "length":2,
            "start":3,
            "value":"明天"
        }
    ],
    "id":"5e7c66efe99bee4962d4069a",
    "intent":"查询天气",
    "text":"上海的明天的天气"
}

```

.conllx 数据格式：
```
#	{"label": "查询天气", "id": "5e7c66efe99bee4962d4069a"}
上	B-地点
海	L-地点
的	O
明	B-日期
天	L-日期
的	O
天	O
气	O
。	O
```
