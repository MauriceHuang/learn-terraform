# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

output "lambda_function_name" {
  value = aws_lambda_function.main.function_name
}

output "lambda_function_arn" {
  value = aws_lambda_function.main.arn
}

output "api_gateway_url" {
  value = "${aws_api_gateway_deployment.main.invoke_url}/${var.api_path}"
  description = "URL to invoke the API Gateway endpoint"
}

output "api_gateway_rest_api_id" {
  value = aws_api_gateway_rest_api.main.id
}