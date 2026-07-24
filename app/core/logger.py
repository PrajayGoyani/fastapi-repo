import logging

def setup_logging():
    """Run this once at application startup to configure global logging behavior."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        force=True # Overwrites any default logging configurations
    )