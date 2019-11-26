provider "google" {
  credentials = "${file("./serviceaccount.json")}"
  project     = "${var.google_project}"
  region      = "${var.google_region}"
}
