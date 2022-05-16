from pandas import DataFrame
from pandasstream.stream import PandasStream as ps

df = (
    ps(data_frame=DataFrame({"Test": ["Hello", "Hello", "Hello"]}))
    .select("Test")
    .mutate(lambda df: {"Test": [100, 150, 150]})
    .as_dataframe()
)
print(df)
