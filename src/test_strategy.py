from strategy.strategy_engine import StrategyEngine



engine = StrategyEngine()



tests = [

    0.1,

    0.45,

    0.85

]



for score in tests:


    result = engine.apply_strategy(
        score
    )


    print(
        "Risk Score:",
        score
    )

    print(result)

    print("-"*40)