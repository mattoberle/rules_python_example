exports_files(["rules_python.patch"])

py_test(
    name = "test",
    srcs = ["test.py"],
    deps = ["@pip_sqlalchemy//:pkg"],
)
