import rpc.configuration as rpcc
import rpc.flightdata as rpcd


def run(id, action_name):
    code_raw = rpcc.load_detect_code(action_name)
    print(code_raw)
    if code_raw is None:
        raise Exception("load code error, check you code name and settings.")

    exec(code_raw)

    param_func = locals().get("setparams")
    detect_func = locals().get("detect")
    if param_func and detect_func:
        params = param_func()
        data = rpcd.load_flight_data(id, params)
        ret = detect_func(data)
        return ret
    return []
