run:
	@uvicorn people.main:app --reload

test:
	@poetry run pytest

unitest:
	@poetry run pytest -s -rx -k $(t) --pdb people ./tests/
