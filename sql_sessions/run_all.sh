#!/bin/bash
echo "🚀 Running all SQL scripts into ecom_retailer.db"
(
  echo ".headers on"
  cat \
    VP_Request/sql_sessions/eda_cleaning.session.sql \
    VP_Request/sql_sessions/eda_core_metrics.session.sql \
    VP_Request/sql_sessions/eda_segementation.session.sql \
    VP_Request/sql_sessions/eda_logistics_summary.session.sql \
    VP_Request/sql_sessions/build_all_dashboards.sql \
    VP_Request/sql_sessions/export_cleaned_tables.sql \
    VP_Request/sql_sessions/export_views.sql
) | sqlite3 ecom_retailer.db