"""Comprehensive demo of Calculator Agent"""
import asyncio
from src.main import CalculatorAgent

async def demo():
    """Runs comprehensive demo of all features"""
    agent = CalculatorAgent()
    
    print("=" * 70)
    print("🎉 CALCULATOR AGENT - COMPREHENSIVE DEMO")
    print("=" * 70)
    print()
    
    tests = [
        ("Basic Math", "15 + 27 * 2"),
        ("Square Root", "What is the square root of 144?"),
        ("Calculus", "!calculus derivative of x^3"),
        ("Linear Algebra", "!linalg determinant [[2,3],[1,4]]"),
        ("Equation Solver", "!solve x^2 - 9 = 0"),
    ]
    
    for name, query in tests:
        print(f"\n{'=' * 70}")
        print(f"🧮 TEST: {name}")
        print(f"{'=' * 70}")
        print(f"Query: {query}")
        print()
        
        result = await agent.process_command(query)
        print(result)
        print()
    
    print("=" * 70)
    print("✅ ALL DEMOS COMPLETED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    asyncio.run(demo())
