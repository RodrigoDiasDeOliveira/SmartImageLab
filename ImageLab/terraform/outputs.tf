# outputs.tf
output "public_ip" {
  description = "IP público da instância"
  value       = oci_core_instance.app_instance.public_ip
}

output "instance_id" {
  description = "ID da instância"
  value       = oci_core_instance.app_instance.id
}
