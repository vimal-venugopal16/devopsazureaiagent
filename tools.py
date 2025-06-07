def simple_calculator(input_string: str) -> str:
    try:
        return str(eval(input_string))
    except:
        return "Error in calculation."

def get_tools():
    from langchain.agents import Tool
    return [
        Tool.from_function(
            func=simple_calculator,
            name="Calculator",
            description="Useful for evaluating basic math expressions. Input should be a math expression like '12 * 3'"
        )
    ]
