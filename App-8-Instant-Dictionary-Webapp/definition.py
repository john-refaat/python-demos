import pandas


class Definition:

    def __init__(self, term):
        self.term = term.lower()

    def get(self):
        df = pandas.read_csv('data.csv')
        return list(df.loc[df['word'] == self.term]['definition'])



if __name__ == '__main__':
    d = Definition('cat')
    print(d.get())