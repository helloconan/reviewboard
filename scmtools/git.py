from reviewboard.diffviewer.parser import DiffParser, DiffParserError, File
from reviewboard.scmtools.core import SCMTool, HEAD, PRE_CREATION
from reviewboard.scmtools.errors import FileNotFoundError, SCMError
                remPrefix = re.compile("^[a|b]/");
                file.origFile = remPrefix.sub("", diffLine[-2])
                file.newFile = remPrefix.sub("", diffLine[-1])