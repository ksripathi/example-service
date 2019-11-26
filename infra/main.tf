resource "google_container_cluster" "primary" {
  name     = "${var.cluster_name}"
  location = "${var.google_region}"
  remove_default_node_pool = true
  initial_node_count = 1
  node_locations = [
    "us-central1-a",
  ]
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "linux-node-pool"
  location   = "${var.google_region}"
  cluster    = "${google_container_cluster.primary.name}"
  node_count = "${var.k8_node_count}"

  node_config {
    preemptible  = true
    machine_type = "${var.node_machine_type}"

    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }
}