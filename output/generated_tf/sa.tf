resource "google_service_account" "demo-service-account" {
  account_id   = "demo-service-account"
  display_name = "Test Service Account"
}


resource "google_project_iam_member" "demo-service-account_1" {
  project = var.project_id
  role    = "roles/storage.admin"
  member  = "serviceAccount:${google_service_account.demo-service-account.email}"
}

resource "google_project_iam_member" "demo-service-account_2" {
  project = var.project_id
  role    = "roles/compute.viewer"
  member  = "serviceAccount:${google_service_account.demo-service-account.email}"
}
