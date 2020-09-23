import wolframalpha



while True:

    a = input("Ask me anything: ")

    app_id = "96KU2A-4W95JTVV98"

    client = wolframalpha.Client(app_id)

    res = client.query(a)

    answer = next(res.results).text

    print(answer)