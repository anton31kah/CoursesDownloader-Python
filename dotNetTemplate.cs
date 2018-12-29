void Main()
{
	CredentialUtil.GetCredential("https://cas.finki.ukim.mk/").Dump();

	new List<int> {1,2,3,5,6,8,10,12,13,14,16}.ConsecutiveGroupBy().Dump();

	// https://html-agility-pack.net/

	// https://github.com/Mpdreamz/shellprogressbar

	// for file type don't use mime, since you'll get file from url, get extension from there, no need for magic
}

public class UserPass
{
	public string UserName { get; set; }
	public string Password { get; set; }

	public UserPass(string username, string password)
	{
		UserName = username;
		Password = password;
	}
}

public static class CredentialUtil
{
	public static UserPass GetCredential(string target)
	{
		var cm = new Credential { Target = target };
		if (!cm.Load())
		{
			return null;
		}

		//UserPass is just a class with two string properties for user and pass
		return new UserPass(cm.Username, cm.Password);
	}

	public static bool SetCredentials(
		 string target, string username, string password, PersistanceType persistenceType)
	{
		return new Credential
		{
			Target = target,
			Username = username,
			Password = password,
			PersistanceType = persistenceType
		}.Save();
	}

	public static bool RemoveCredentials(string target)
	{
		return new Credential { Target = target }.Delete();
	}
}

public static class MoreIterTools
{
	public static IEnumerable<IEnumerable<int>> ConsecutiveGroupBy(this IEnumerable<int> iterable)
	{
		return iterable.Distinct()
					   .OrderBy(i => i)
					   .Select((i, idx) => new {i, key = i - idx})
					   .GroupBy(tuple => tuple.key, tuple => tuple.i);
	}
}
