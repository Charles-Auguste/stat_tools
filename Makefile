clean:
	@bash -c 'delete_pycache() { \
	    for dir in "$$1"/*; do \
	        if [ -d "$$dir" ]; then \
	            if [ "$$(basename "$$dir")" = "__pycache__" ]; then \
	                rm -rf "$$dir"; \
	                echo "Deleted: $$dir"; \
	            else \
	                delete_pycache "$$dir"; \
	            fi; \
	        fi; \
	    done; \
	}; \
	delete_pycache .'
	@rm -rf build
	@rm -rf dist
	@rm *.spec

# Development workflow
setup:
	@conda create -n sa-cva

dev_install:
	@poetry lock
	@poetry install
	@git config --local --unset core.hooksPath | true
	@git config --global --unset core.hooksPath | true
	@pre-commit install
	@.git/hooks/pre-commit

test:
	@coverage run --source=stat_tools -m pytest -v tests && coverage report -m

# QA
qa_check_code:
	@flake8 .

format_code:
	@isort .
	@black .

# Production deploy tools ( Used by CI )
#
install: clean wheel
	@pip3 install -U dist/*.whl --cache-dir /pip_cache

wheel: clean
	@poetry build

wheel_upload: clean wheel
	@TWINE_PASSWORD=${CI_JOB_TOKEN} TWINE_USERNAME=gitlab-ci-token python3 -m twine upload --repository-url ${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/packages/pypi dist/* --skip-existing
