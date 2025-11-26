"""Developer helper script for common project tasks.
Usage examples:
  python dev_tasks.py test
  python dev_tasks.py demo
  python dev_tasks.py coverage
"""
import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
PYTHON = sys.executable

def run(cmd: list[str]):
    print(f"\n[run] {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def task_test():
    run([PYTHON, '-m', 'pytest', 'tests', '-v'])


def task_coverage():
    run([PYTHON, '-m', 'pytest', '--cov=src', '--cov-report=term-missing'])


def task_demo():
    run([PYTHON, 'demo.py'])


def main():
    if len(sys.argv) < 2:
        print("Kullanım: python dev_tasks.py <test|coverage|demo>")
        raise SystemExit(1)
    cmd = sys.argv[1].lower()
    if cmd == 'test':
        task_test()
    elif cmd == 'coverage':
        task_coverage()
    elif cmd == 'demo':
        task_demo()
    else:
        print(f"Bilinmeyen komut: {cmd}")
        raise SystemExit(1)

if __name__ == '__main__':
    main()
