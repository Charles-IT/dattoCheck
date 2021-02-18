
# Global Variables
API_BASE_URI = 'https://api.datto.com/v1/bcdr/device'
XML_API_BASE_URI = 'https://portal.dattobackup.com/external/api/xml/status'

# Error/Alert threshold settings
CHECKIN_LIMIT = 60 * 20                  # threshold for device offline time
STORAGE_PCT_THRESHOLD = 95               # threshold for local storage; in percent
LAST_BACKUP_THRESHOLD = 60 * 60 * 12     # threshold for failed backup time
LAST_OFFSITE_THRESHOLD = 60 * 60 * 72    # threshold for last successful off-site
LAST_SCREENSHOT_THRESHOLD = 60 * 60 * 48 # threshold for last screenshot taken
ACTIONABLE_THRESHOLD = 60 * 60 * 24 * 7  # threshold for actionable alerts; one week

# Define errors
class Error(Exception):
	"""Base class for errors/exceptions"""
	pass

class DattoApiError(Error):
	"""Raised on errors encountered from the Datto API."""
	pass
