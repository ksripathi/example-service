variable "linux_admin_username" {
    type = "string"
    description = "User name for authentication to the Kubernetes linux agent virtual machines in the cluster."
}
variable "linux_admin_password" {
   type ="string"
   description = "The password for the Linux admin account."
}
variable "k8_node_count" {
   type = "string"
   description = "total number of nodes in the k8 cluster"
}
variable "google_project" {
   type = "string"
   description = "configure google project id"
}
variable "google_region" {
   type = "string"
   description = "setup the google region"
}
variable "cluster_name" {
   type = "string"
   description = "Cluster name for the GCP Cluster."
}
variable "node_machine_type" {
   type = "string"
   description = "type of VM required"
}
