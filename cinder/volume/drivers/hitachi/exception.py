# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Cinder base exception handling.

Includes decorator for re-raising Cinder-type exceptions.

SHOULD include dedicated exception logging.

"""

from cinder import exception
from cinder.i18n import _



# Hitachi Block Storage Driver
class HBSDError(exception.VolumeDriverException):
    message = _("HBSD error occurs.")


class HBSDCmdError(HBSDError):

    def __init__(self, message=None, ret=None, err=None):
        self.ret = ret
        self.stderr = err

        super(HBSDCmdError, self).__init__(message=message)


class HBSDBusy(HBSDError):
    message = "Device or resource is busy."


class HBSDNotFound(exception.NotFound):
    message = _("Storage resource could not be found.")


class HBSDVolumeIsBusy(exception.VolumeIsBusy):
    message = _("Volume %(volume_name)s is busy.")


# Hitachi VSP Driver
class VSPError(exception.VolumeDriverException):
    message = _("VSP error occurred. %(message)s")


class VSPBusy(VSPError):
    message = _("Device or resource is busy.")


class VSPNotSupported(VSPError):
    message = _("The function on the storage is not supported.")

