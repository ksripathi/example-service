resource "google_container_cluster" "primary" {
  name     = "${var.cluster_name}"
  location = "us-central1"
  remove_default_node_pool = true
  initial_node_count       = 1
  node_locations = [
    "us-central1-a",
  ]
}

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "my-node-pool"
  location   = "us-central1"
  cluster    = "${google_container_cluster.primary.name}"
  node_count = 2

  node_config {
    preemptible  = true
    machine_type = "n1-standard-4"

    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring",
    ]
  }
}